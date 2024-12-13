import csv

with open('page_ordering_rules.txt', 'r') as ordering_input, open('page_production_order.txt', 'r') as production_input:
    ordering_reader = csv.reader(ordering_input, delimiter='|')
    production_reader = csv.reader(production_input)

    order = {}

    for row in ordering_reader:
        before, after = row[0], row[1]
        
        if before not in order:
            order[before] = []
        
        order[before].append(after)
    
    middle_pages_total = 0
    incorrect_rows = []
    for row in production_reader:
        page_index_map = {}

        # Make the index map
        for index, page in enumerate(row):
            page_index_map[page] = index

        # Assume the production order is correct
        correct_order = True
        
        for index, page in enumerate(row):
            # If we've already proven it's incorrect, we can stop processing
            if not correct_order:
                break

            # If a page doesn't have any other pages it needs to be before, we can skip
            if page in order:
                curr_order_rules = order[page]
            else:
                continue
            
            # Check each page that must come after and confirm that if it appears, it comes after
            for after_page in curr_order_rules:
                # If it comes before the current page, we know the order is incorrect and can break
                if after_page in page_index_map and page_index_map[after_page] < index:
                    correct_order = False
                    incorrect_rows.append(row)
                    break
            
        if correct_order:
            middle_index = len(row) // 2
            middle_pages_total += int(row[middle_index])
    
    print('Question 1 Answer: ', middle_pages_total)

    def get_correct_order(production_order):

        index_map = {}
        
        for index, page in enumerate(production_order):
            index_map[page] = index

        i, j = -1, -1

        for index, page in enumerate(production_order):
            if i > 0 or j > 0:
                break

            # If the page isn't in the dict, it means it does not need to come before any other page
            if page not in order:
                continue

            after_pages = order[page]

            for after_page in after_pages:
                if (after_page in index_map) and (index_map[after_page] < index):
                    i, j = index, index_map[after_page]
                    break
        
        if i < 0:
            return production_order
        else:
            production_order[i], production_order[j] = production_order[j], production_order[i]
            return get_correct_order(production_order)

    corrected_row_total = 0
    for row in incorrect_rows:
        correct_row = get_correct_order(row)
        corrected_row_total += int(correct_row[len(row) // 2])

    print('Question 2 Answer: ', corrected_row_total)


