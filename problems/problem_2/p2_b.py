def binary_search(packages, boxes):
    def binary_search_algo(boxes, package):
      low, high = 0, len(boxes) - 1
      while low < high:
          mid = (low + high) // 2
          if boxes[mid] < package:
              low = mid + 1
          else:
              high = mid
      return low

    suppliers_waste_lst = []
    num_suppliers_fail_int = 0

    for supplier in boxes:
        supplier_waste_int = 0
        sorted_boxes = sorted(supplier)

        for package in packages:
            if package > sorted_boxes[-1]:
                num_suppliers_fail_int += 1
                break

            index = binary_search_algo(sorted_boxes, package)
            supplier_waste_int += sorted_boxes[index] - package

        suppliers_waste_lst.append(supplier_waste_int)
    
    if num_suppliers_fail_int == len(boxes):
        return -1
    else:
        return min(suppliers_waste_lst)  