def hoy_comemos_mejillones(parameter_list):
    """Cuenta la cantidad de montones de mejillones
        
        Params:
            val (tuple) : Tupla con los tamaños de los mejillones
        Return:
            val (int) : Devuelve el numero de montones
        """
    largo = len(parameter_list)
    count = 1
    n = 0

    while n < largo:
        try:
            num1 = parameter_list[n]
            num2 = parameter_list[n+1]

            if num2 >= num1:
                count += 1

        except:
            pass
        n += 1
    
    return count
