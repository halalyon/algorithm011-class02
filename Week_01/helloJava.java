package Week_01;

import java.util.ArrayDeque;
import java.util.Deque;
// import java.util.PriorityQueue;

/**
 * deque
 */
public class helloJava {

    public static void main(String[] args) {
        // instantiate a queue
        Deque<String> queue = new ArrayDeque<String>();
        queue.addFirst("a");
        queue.addFirst("b");
        queue.addFirst("c");
        System.out.println(queue);
        String elem = queue.pollFirst();
        System.out.println(elem);

        // instantiate a stack
        Deque<String> stack = new ArrayDeque<String>();
        stack.addLast("a");
        stack.addLast("b");
        stack.addLast("c");
        System.out.println(stack);
        elem = stack.pollLast();
        // System.out.println(elem);
        System.out.println((10-1)<<1);
        
    }
}