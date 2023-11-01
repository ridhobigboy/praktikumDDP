def cari_bilangan_prima (awal,akhir):
    list_bilangan_prima = []

    for x in range(awal,akhir+1):
        if is_prima(x):
            list_bilangan_prima.append(x)

            return list_bilangan_prima