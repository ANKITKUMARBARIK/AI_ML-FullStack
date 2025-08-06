"""

Some chai flavors are out of stock.

You want to skip those and stop entirely if
someone requests a restricted flavor.

Task:
• Skip if flavor is "Out of Stock"
• Break if flavor is "Discontinued"

"""

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")

print(f"Out side of loop")



"""

Parcel Scanning System------------->
You are automating a parcel scanning system in a warehouse. Each parcel has a barcode. The system must validate all parcels and report issues:

Tasks:

- There is list named parcel_code which consist of barcods.
- The system will go through each barcode in the list using a for loop:
If a barcode is "DAMAGED", skip it using continue and log: "Skipped damaged parcel".
If a barcode is "STOP", use break and log: "Critical error: Stopping scan".
For valid barcodes, log: "Scanned parcel: <barcode>".
- If the loop completes without hitting a break, log: "All parcels scanned successfully" using for-else.
- Return a list of all scan messages.

"""

# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    # Write your code below this line
    new_lists = []
    
    for barcode in parcel_codes:
        if barcode == "DAMAGED":
            new_lists.append(f"Skipped damaged parcel")
            continue
        if barcode == "STOP":
            new_lists.append(f"Critical error: Stopping scan")
            break
        new_lists.append(f"Scanned parcel: {barcode}")
    else:
        new_lists.append(f"All parcels scanned successfully")
        
    return new_lists

print(f"{scan_parcels(["GOOD1","GOOD2","DAMAGED","GOOD4","STOP","GOOD6"])}")
