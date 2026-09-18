package Generics4;

public class MyArrayList3 implements MyInterface<String> {
    private Object[] elements = new Object[10];
    private int size = 0;

    public MyArrayList3() {
    }

    @Override
    public void add(String element) {
        if (size == elements.length) {
            Object[] newElements = new Object[elements.length * 2];
            System.arraycopy(elements, 0, newElements, 0, elements.length);
            elements = newElements;
        }
        elements[size++] = element;
    }

    @Override
    public String get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("索引越界");
        }
        return (String) elements[index];
    }

    @Override
    public int size() {
        return size;
    }
}

interface MyInterface<E> {
    void add(E element);
    E get(int index);
    int size();
}

// 测试类（可添加）
class Test {
    public static void main(String[] args) {
        MyArrayList3 list = new MyArrayList3();
        list.add("Java");
        list.add("泛型");
        System.out.println("元素个数：" + list.size());
        System.out.println("第一个元素：" + list.get(0));
    }
}





