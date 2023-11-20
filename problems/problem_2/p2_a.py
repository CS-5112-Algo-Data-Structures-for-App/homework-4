def linear_search(packages, boxes):
  suppliers_waste_lst = []
  num_suppliers_fail_int = 0

  for supplier in boxes:
    supplier_waste_int = 0
    sorted_boxes = sorted(supplier)

    for package in packages:
      if package > sorted_boxes[-1]:
        num_suppliers_fail_int += 1
        break

      for box in sorted_boxes:
        if package <= box:
          supplier_waste_int += box - package
          break

    suppliers_waste_lst.append(supplier_waste_int)
  
  if num_suppliers_fail_int == len(boxes):
    return -1
  else:
    return min(suppliers_waste_lst)
      
          



# if __name__ == '__main__':

#   boxes = [[12],[11,9],[10,5,14]]
#   packages = [3,5,8,10,11,12]

#   result = linear_search(packages, boxes)

#   print(result)
      