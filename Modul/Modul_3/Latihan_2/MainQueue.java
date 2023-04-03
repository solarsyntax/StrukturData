package Modul.Modul_3.Latihan_2;

import java.util.Queue;
import java.util.LinkedList;

public class MainQueue {
    public void queueExample() {
        Queue queue = new LinkedList();
        queue.add("java");
        queue.add("DotNet");
        queue.offer("PHP");
        queue.offer("HTML");
        System.out.println("Remove: " + queue.remove());
        System.out.println("Element: " + queue.element());
        System.out.println("Poll: " + queue.poll());
        System.out.println("Peek: " + queue.peek());

    }

    public static void main(String[] args) {
        new MainQueue().queueExample();
    }
}
