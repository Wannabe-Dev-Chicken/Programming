initialized = True

while initialized:
    ogcmd = input('Task for a program to complete? (Type "options" for a list of available tasks, or hit Return\Enter to exit)\n')
    cmd = ogcmd.lower()
    if cmd == "options":
        print("""The available tasks are:
    1. find the absolute value of an integer
    2. find an async iterator for an async iterable
    3. find the binary representation of an integer
    4. find out if an object can be run
    5. find the character representation of an integer
    6. delete an attribute from an object
    7. find the attributes of an object
    8. find both the quotient and the remainder of a division operation
    9. find an attribute from an object
    10. find if an object has an attribute
    11. find the hash value of an object
    12. find the hexadecimal representation of an integer
    12. find the identity of an object
    14. print out a prompt and read a string from standard input
    15. find whether an object is an instance of a class
    16. find whether 'cls' is derived from another class or is the same class
    17. find an iterator for an iterable
    18. find the largest item in an iterable
    19. find the smallest item in an iterable
    20. find the octal representation of an integer
    21. find the Unicode code point for a one-character string
    22. find 'base' raised to the power of 'exponent'
    23. print out an object
    24. terminate the program
    25. round a float to the nearest whole number
    26. set an attribute of an object to a value
    27. find a copy of a list sorted into ascending order
    28. find the sum of the items in a list""")

    if cmd == "find the absolute value of an integer":
        print("""Python:
    print(abs(integer))
Java:
    public static void main(String[] args) {
        System.out.println(Math.abs(integer));
    }""")
    
    if cmd == "find an async iterator for an async iterable":
        print("""Python:
    print(aiter(async iterable))
Java:
    public static void main(String[] args) {
        System.out.println(async iterable.iterator());
    }""")
    
    if cmd == "find the binary representation of an integer":
        print("""Python:
    print(bin(integer))
Java:
    public static void main(String[] args) {
        System.out.println(Integer.toBinaryString(integer));
    }""")
    
    if cmd == "find out if an object can be run":
        print("""Python:
    print(callable(object))
Java:
    public static void main(String[] args) {
        Runnable object = () -> {
            System.out.println("True");
        };
        object.run();
    }""")
    
    if cmd == "find the character representation of an integer":
        print("""Python:
    print(chr(integer))
Java:
    public static void main(String[] args) {
        System.out.println((char) integer);
    }""")
    
    if cmd == "delete an attribute from an object":
        print("""Python:
    delattr(object, "attribute")
Java:
    public static void delattr(Object obj, String attributeName) throws NoSuchFieldException, IllegalAccessException {
        Class<?> clazz = obj.getClass();
        Field field = clazz.getDeclaredField(attributeName);
        field.setAccessible(true);
        field.set(obj, null);
    }
    
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        delattr(object, "attribute");
    }""")
    
    if cmd == "find the attributes of an object":
        print("""Python:
    print(dir(object))
Java:
    public static void dir(Object obj) {
        Class<?> clazz = obj.getClass();

        for (Constructor<?> constructor : clazz.getDeclaredConstructors()) {
            System.out.println("  " + constructor.toString());
        }

        for (Field field : clazz.getDeclaredFields()) {
            System.out.println("  " + field.toString());
        }

        for (Method method : clazz.getDeclaredMethods()) {
            System.out.println("  " + method.toString());
        }
    }

    public static void main(String[] args) {
        dir(object);
    }""")
        
    if cmd == "find both the quotient and the remainder of a division operation":
        print("""Python:
    print(divmod(dividend, divisor))
Java:
    public static int[] divmod(int dividend, int divisor) {
        int quotient = dividend / divisor;
        int remainder = dividend % divisor;
        return new int[] {quotient, remainder};
    }

    public static void main(String[] args) {
        int dividend = 17;
        int divisor = 5;
        int[] result = divmod(dividend, divisor);
        System.out.println("(" + result[0] + ", ");
        System.out.println(result[1] + ")");
    }""")
        
    if cmd == "find an attribute from an object":
        print("""Python:
    print(getattr(object, "attribute"))
Java:
    public static Object getAttribute(Object obj, String fieldName) {
        Class<?> clazz = obj.getClass();
        try {
            Field field = clazz.getDeclaredField(fieldName);
            field.setAccessible(true);
            return field.get(obj);
        } catch (NoSuchFieldException | IllegalAccessException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        System.out.println(getAttribute(object, "attribute"));
    }""")
        
    if cmd == "find if an object has an attribute":
        print("""Python:
    print(hasattr(object, "attribute"))
Java:
    public static void hasAttribute(Object obj, String attributeName) {
        try {
            Field field = obj.getClass().getField(attributeName);
            System.out.println("true");
        }
        catch (NoSuchFieldException e) {
            System.out.println("False");
        }
    }

    public static void main(String[] args) {
        hasAttribute(object, "attribute");
    }""")
        
    if cmd == "find the hash value of an object":
        print("""Python:
    print(hash(object))
Java:
    public static void main(String[] args) {
        System.out.println(object.hashCode());
    }""")
        
    if cmd == "find the hexadecimal representation of an integer":
        print("""Python:
    print(hex(integer))
Java:
    public static void main(String[] args) {
        System.out.println(Integer.toHexString(integer));
    }""")
        
    if cmd == "find the identity of an object":
        print("""Python:
    print(id(object))
Java:
    public static void main(String[] args) {
        System.out.println(System.identityHashCode(object));
    }""")
        
    if cmd == "print out a prompt and read a string from standard input":
        print("""Python:
    input(prompt)
Java:
    public static void main(String[] args) {
        System.out.println("prompt");
        new Scanner(System.in).nextLine();
    }""")
        
        
    if cmd == "find whether an object is an instance of a class":
        print("""Python:
    print(isinstance(object, class))
Java:
    public static void main(String[] args) {
        boolean instof = object instanceof class;
        if (instof == true) {
            System.out.println("True");
        }
        if (instof == false) {
            System.out.println("False");
        }
    }""")
        
    if cmd == "find whether 'cls' is derived from another class or is the same class":
        print("""Python:
    print(issubclass(cls, class))
Java:
    public static void main(String[] args) {
        System.out.println(cls.class.isAssignableFrom(class.class);
    }""")
        
    if cmd == "find an iterator for an iterable":
        print("""Python:
    print(iter(iterable))
Java:
    public static void main(String[] args) {
        System.out.println(iterable.iterator());
    }""")
        
    if cmd == "find the largest item in an iterable":
        print("""Python:
    print(max(iterable))
Java:
    public static void main(String[] args) {
        System.out.println(Collections.max(iterable));
    }""")
        
    if cmd == "find the smallest item in an iterable":
        print("""Python:
    print(min(iterable))
Java:
    public static void main(String[] args) {
        System.out.println(Collections.min(iterable));
    }""")
    
    if cmd == "find the octal representation of an integer":
        print("""Python:
    print(oct(integer))
Java:
    public static void main(String[] args) {
        System.out.println(Integer.toOctalString(integer));
    }""")
    
    if cmd == "find the Unicode code point for a one-character string":
        print("""Python:
    print(ord("character"))
Java:
    public static void main(String[] args) {
        System.out.println((int) 'character');
    }""")
    
    if cmd == "find 'base' raised to the power of 'exponent'":
        print("""Python:
    print(pow(base, exponent))
Java:
    public static void main(String[] args) {
        System.out.println((float) Math.pow(base, exponent));
    }""")
    
    if cmd == "print out an object":
        print("""Python:
    print(object)
Java:
    public static void main(String[] args) {
        System.out.println(object);
    }""")
    
    if cmd == "terminate the program":
        print("""Python:
    quit()
Java:
    public static void main(String[] args) {
        System.exit(0);
    }""")

    if cmd == "round a float to the nearest whole number":
        print("""Python:
    print(round(float, None))
Java:
    public static void main(String[] args) {
        System.out.println(Math.round(float));
    }""")

    if cmd == "set an attribute of an object to a value":
        print("""Python:
    setattr(object, "attribute", value)
Java:
    public static void setattr(Object obj, String attributeName, Object value) throws NoSuchFieldException, IllegalAccessException {    
        Class<?> clazz = obj.getClass();
        Field field = clazz.getDeclaredField(attributeName);
        field.setAccessible(true);
        field.set(obj, value);
    }
    
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        setattr(object, "attribute", value);
    }""")
        
    if cmd == "find a copy of a list sorted into ascending order":
        print("""Python:
    print(sorted(list))
Java:
    public static void main(String[] args) {
        List<Integer> copy = new ArrayList<>(list);
        Collections.sort(copy);
        System.out.println(copy);
    }""")

    if cmd == "find the sum of the items in a list":
        print("""Python:
    print(sum(list))
Java:
    public static void main(String[] args) {
        System.out.println(list.stream().reduce(0, Integer::sum));
    }""")

    if cmd == "":
        quit()
        
    else:
        print(f'"{ogcmd}" is not recognized as a task.  (Try typing "options" and copy-pasting the task that you want, (without the number) into the program.)')