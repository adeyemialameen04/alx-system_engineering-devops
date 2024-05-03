def safe_print_list(mylist=[], x = 0):
    no_count = 0;
    try:
        for i, element in enumerate(mylist):
            if no_count < x:
                print("{}".format(element), end='')
                no_count += 1
    except Exception:
        pass
