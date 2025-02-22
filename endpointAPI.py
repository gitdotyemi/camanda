from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

# Define Pydantic models for data validation
class Order(BaseModel):
    orderID: str
    customerName: str
    customerID: str
    pickupLocation: str
    pickupDate: str
    dropoffLocation: str
    dropoffDate: str
    orderStatus: str

class Vehicle(BaseModel):
    vehicleID: str
    registrationNumber: str
    makeModel: str
    year: str
    capacity: int
    fuelType: str
    fuelEfficiency: float
    vehicleStatus: str

class Driver(BaseModel):
    driversID: str
    driversName: str
    phoneNumber: str
    licenseNumber: str
    vehicleQualification: str
    driverStatus: str
    yearsOfExperience: int

class DataInput(BaseModel):
    orders: List[Order]
    vehicles: List[Vehicle]
    drivers: List[Driver]

# Database connection function
def connect_db():
    return sqlite3.connect("tripManagement.db")

# API endpoint to receive and store data
@app.post("/store_data/")
async def store_data(data: DataInput):
    conn = connect_db()
    c = conn.cursor()

    try:
        # Insert orders data
        for order in data.orders:
            c.execute("""
                INSERT INTO orders (orderID, customerName, customerID, pickupLocation, pickupDate, dropoffLocation, dropoffDate, orderStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (order.orderID, order.customerName, order.customerID, order.pickupLocation, order.pickupDate, order.dropoffLocation, order.dropoffDate, order.orderStatus))

        # Insert vehicles data
        for vehicle in data.vehicles:
            c.execute("""
                INSERT INTO vehicles (vehicleID, registrationNumber, makeModel, year, capacity, fuelType, fuelEfficiency, vehicleStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (vehicle.vehicleID, vehicle.registrationNumber, vehicle.makeModel, vehicle.year, vehicle.capacity, vehicle.fuelType, vehicle.fuelEfficiency, vehicle.vehicleStatus))

        # Insert drivers data
        for driver in data.drivers:
            c.execute("""
                INSERT INTO drivers (driversID, driversName, phoneNumber, licenseNumber, vehicleQualification, driverStatus, yearsOfExperience)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (driver.driversID, driver.driversName, driver.phoneNumber, driver.licenseNumber, driver.vehicleQualification, driver.driverStatus, driver.yearsOfExperience))

        conn.commit()
        return {"message": "Data stored successfully!"}

    except sqlite3.Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

    finally:
        conn.close()