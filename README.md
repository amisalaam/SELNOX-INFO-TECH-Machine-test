# SELNOX-INFO-TECH-Machine-test


## Overview

The Vendor Management System (VMS) helps manage vendor information, purchase orders, and performance metrics. This system tracks vendor performance over time and provides data-driven insights.

## Features

- Create, retrieve, update, and delete vendors
- Create, retrieve, update, and delete purchase orders
- Track and calculate vendor performance metrics
- Record historical performance data for trend analysis

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

## 1. Clone the repository:

     git clone https://github.com/yourusername/vms.git
     cd vms
   
## 2. Create and activate a virtual environment:
     python -m venv venv
     source venv/bin/activate

## 3. Install the required packages:
     pip install -r requirements.txt

## 4. Run migrations:
     python manage.py migrate

## 5. Create a superuser:
    python manage.py createsuperuser

## 6. Run the development server:
     python manage.py runserver


 ## API Endpoints

 ### Vendor Endpoints

 - POST /vendors/: Create a new vendor
 - GET /vendors/: Retrieve all vendors
 - GET /vendors/<vendor_id>/: Retrieve a specific vendor by ID
 - PUT /vendors/<vendor_id>/: Update a specific vendor by ID
 - DELETE /vendors/<vendor_id>/: Delete a specific vendor by ID

### Purchase Order Endpoints

- POST /purchase_order/: Create a new purchase order
- GET /purchase_order/: Retrieve all purchase orders
- GET /purchase_order/<po_id>/: Retrieve a specific purchase order by ID
- PUT /purchase_order/<po_id>/: Update a specific purchase order by ID
- DELETE /purchase_order/<po_id>/: Delete a specific purchase order by ID

  
### Performance Metrics Endpoint

- GET /vendors/<vendor_id>/performance/: Retrieve performance metrics for a specific vendor by ID
  
### Purchase Order Acknowledge Endpoint

- POST /purchase_orders/<po_id>/acknowledge/: Update acknowledgment date for a purchase order

   

    

    

   
