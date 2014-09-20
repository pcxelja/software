for i in range(1, 101):

    if not i % 3:

        if not i % 5:

            print "FizzBuzz"

        else:

            print "Fizz"

    elif not i % 5:

        print "Buzz"

    else:

        print i


#1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz
