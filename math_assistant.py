def math_assistant():
  answear = input('enter the number of the option you want me to help you with ? ______ 1-calculations , 2-areas , 3-perimeters , 4-distances , 5-units , 6-even or odd : ')
  if answear == '1':
    number1 = int(input('enter number 1 :'))
    number2 = int(input('enter number 2 :'))
    the_operation = input('+,-,/,*,** :')
    if the_operation == '+':
      print (number1 + number2)
    if the_operation == '-':
      print (number1 - number2)
    if the_operation == '*':
      print (number1 * number2)
    if the_operation == '/':
      print (number1 / number2)
    if the_operation == '**':
      print (number1 ** number2)
    if the_operation != ('+' or '-' or '*' or '/' or '**'):
      print ('the operation you entered is incorrect')
  if answear == '3':
    print ('1-square , 2-triangle , 3-circle , 4-rectangle , 5-rhombus , 6-parallelogram:')
    answear2 = input('enter the number of the option :')
    if answear2 == '1':
      s_side = int(input('enter the side of the square :'))
      s_perimeter = s_side * 4
      print ('the perimeter of the square equal')
      print (s_side)
    if answear2 == '2':
      t_side1 =int(input('enter side1 of the triangle :'))
      t_side2 =int(input('enter side2 of the triangle :'))
      t_side3 =int(input('enter side3 of the triangle :'))
      t_perimeter = t_side1 + t_side2 + t_side3
      print ('the perimeter of the triangle equal')
      print (t_perimeter)
    if answear2 == '4':
       r_lenght = int(input('enter the lenght of the rectangle :'))
       r_width = int(input('enter the width of the rectangle :'))
       r_perimeter = r_lenght + r_width 
       r_perimeter1 = r_perimeter * 2
       print ('the perimeter of the rectangle equal')
       print (r_perimeter1)
    if answear2 == '3':
          c_R = int(input('enter the R of the circle :'))
          c_perimeter = 2 * c_R 
          c_perimeter1 = c_perimeter * 3.14
          print ('the perimeter of the circle aqual')
          print(c_perimeter1)
    if answear2 == '6':
      p_base = int(input('enter the base of the parallelogram :'))
      p_side = int(input('enter the side of the parallelogram :'))
      p_perimeter = p_base + p_side 
      p_perimeter1 = p_perimeter * 2
      print ('the perimeter of the parallelogram equal')
      print (p_perimeter1)
    if answear2 == '5':
      r_side1 = int(input('enter side1 of the rhombus :'))
      r_side2 = int(input('enter side2 of the rhombus :'))
      r_side3 = int(input('enter side3 of the rhombus :'))
      r_side4 = int(input('enter side4 of the rhombus :'))
      r_rhombus = r_side1 + r_side2 + r_side3 + r_side4
      print ('the perimeter of the rhombus equal')
      print (r_rhombus)
    if answear2 == None:
      print ('the number you typed is not exist in options')
  if answear == '2':
    print('1-square , 2-triangle , 3-rectangle , 4-circle , 5-rhombus , 6-parallelogram:')
    answear3 = input('enter the number of the option :')
    if answear3 == '1':
       s_a_side = int(input('enter the side of the square :'))
       a_square = s_a_side * s_a_side
       print ('the area of the square equal')
       print (a_square)
    elif answear3 == '2':
      t_a_height = int(input('enter the height of the triangle :'))
      t_a_base = int(input('enter the base of the triangle :'))
      a_triangle = t_a_base * t_a_height 
      a_triangle1 = a_triangle / 2
      print ('the area of the triangle equal')
      print (a_triangle1)
    elif answear3 == '3':
      r_a_lenght = int(input('enter the lenght of the rectangle :'))
      r_a_width = int(input('enter the width of the rectangle :'))
      a_rectangle = r_a_lenght * r_a_width
      print ('the area of the rectangle equal')
      print (a_rectangle)
    elif answear3 == '4':
      c_R_a = int(input('enter the R of the circle :'))
      a_c = c_R_a ** 2 
      a_c1 = a_c * 3.14
      print ('the area of the circle equal')
      print (a_c1)
    elif answear3 == '6':
      h_parallelogram = int(input('enter the height of the parallelogram :'))
      b_parallelogarm = int(input('enter the base of the parallelogram :'))
      a_parallelogram = h_parallelogram * b_parallelogarm
      print ('the area of the parallelogram equal')
      print (a_parallelogram)
    elif answear3 == '5':
      h_rhombus = int(input('enter the height of the rhombusm :'))
      s_rhombus = int(input('enter the side of the rhombus :'))
      a_rhombus = h_rhombus * s_rhombus
      print ('the area of the rhombus equal')
      print(a_rhombus)
    elif answear3 != ('square' or 'triangle' or 'rectangle' or 'circle'):
      print ('the word you typed is incorrect or is not among the options')
  if answear == '4':
    print('1-speed or 2-distance or 3-time :')
    answear4 = input('enter the number of the option :')
    if answear4 == '1':
      distance1 = int(input('enter the distance in km :'))
      time1 = int(input('enter the time in hours :'))
      speed1 = distance1 / time1 
      print ('the speed equal')
      print(speed1)
      print ('km/h')
    if answear4 == '2':
      speed2 = int(input('enter the speed in km/h :'))
      time2 = int(input('enter the time in hours :'))
      distance2 = speed2 * time2
      print ('the distance equal')
      print (distance2)
      print('km')
    if answear4 == '3':
      speed3 = int(input('enter the speed in km/h :'))
      distance3 = int(input('enter the distance in km :'))
      time3 = distance3 / speed3 
      print ('the time equal')
      print (time3)
      print ('hours')
    else :
      print ('the number you typed is not exist in options')

  if answear == '5':
    print ('1-time , 2-lenght :')
    answear5 = input('enter the number of the option :')
    if answear5 == '1':
      print ('1-from seconds to minutes 2-from minutes to hours 3- from hours to minutes 4-from minutes to seconds')
      options1 = input('enter the number of the option :')
      if options1 == '1':
        seconds1 = int(input('enter the seconds :'))
        minutes1 = seconds1 /60
        print (minutes1)
        print ('menutes')
      elif options1 == '2':
        minutes2 = int(input('enter the minutes :'))
        hours1 = minutes2 /60
        print(hours1)
        print ('hours')
      elif options1 == '3':
        hours2 = int(input('enter the hours'))
        minutes3 = hours2 *60
        print (minutes3)
        print('minutes')
      elif options1 == '4':
        minutes4 = int(input('enter the minutes :'))
        seconds2 = minutes4 *60
        print (seconds2)
        print ('seconds')
      else:
        print('the number you typed is not exist in options')
    if answear5 == '2':
      print ('1-from centimeters to inchs 2-from inchs to centimeters 3-from centimeters to metres 4-from meters to kilometers 5-from kilometers to miles 6-from miles to kilometers 7-from kilometers to meters')
      options2 = input('enter the number of the option :')
      if options2 == '1':
        centimeters1 = int(input('enter the centimeters :'))
        inchs1 = centimeters1 /2.54
        print (inchs1)
        print ('inches')
      elif options2 == '2':
        inchs2 = int(input('enter the inchs :'))
        centimeters2 = inchs2 *2.54
        print (inchs2)
        print ('cm')
      elif options2 == '3':
        centimeters3 = int(input('enter the centimeters :'))
        meters1 = centimeters3 /100
        print (meters1)
        print('m')
      elif options2 == '4':
        meters2 = int(input('enter the meters :'))
        kilometers1 = meters2 /1000
        print (kilometers1)
        print ('km')
      elif options2 == '5':
        kilometers2 = int(input('enter the kilometers :'))
        miles1 = kilometers2 /1.6093
        print(miles1)
        print('miles')
      elif options2 == '6':
        miles2 = int(input('enter the miles :'))
        kilometers3 = miles2 *1.6093
        print(kilometers3)
        print('km')
      elif options2 == '7':
        kilometers4 = int(input('enter the kilometers'))
        meters3 = kilometers4 *1000
        print(meters3)
        print('m')
      else:
        print ('the number you typed is not exist in options')

  if answear == '6':
    even_odd = input('enter the number :')
    if even_odd % 2 == 0:
      print('number', even_odd ,'is even')
    elif even_odd % 2 != 0:
      print('number', even_odd ,'is odd')
    else:
      print('the number you entered is incorrect')