学习笔记
1.使用addFirst and addLast重写Deque双端队列代码
见helloJava

2.分析Queue和Priority Queue的java代码
Queue是个可复用接口，具体工程实现由多个类实现，下面的接口类均由各个类去实现即可
boolean add(E e);
boolean offer(E e);
上述方法均是将制定元素插入队列的方法，并且返回一个bool值，表示是否插入成功。两种方法唯一的区别是
add方法在队列满的时候插入会报异常，而offer方法则会返回false。所以，java官方倾向于推荐
使用offer方法。
E remove();
E poll();
上述方法均是获取队列首元素并且将其删除的方法，返回该元素。两种方法的区别是，remove方法在队列空的时候删除队首元素会报异常，而poll方法直接返回空元素。
E element();
E peek();
上述方法是获取队列首元素并且将其返回。两种方法区别是，element方法在队列空的时候删除队首元素会报异常，而peek方法直接返回空元素。


Priority Queue是个有限队列的类，主要有两种调用方法add和poll
add方法，添加元素到队列尾部，并且维护优先队列的二叉平衡堆，时间复杂度为O(1)
下面是维护二叉平衡堆的内部函数，主要将添加的元素能够跟其父节点进行比较，如果小就和父节点进行对调，依次向上进行，由于只跟父节点进行比较，所以复杂度维持在了常数范围内
    private static <T> void siftUpComparable(int k, T x, Object[] es) {
        Comparable<? super T> key = (Comparable<? super T>) x;
        while (k > 0) {
            int parent = (k - 1) >>> 1;
            Object e = es[parent];
            if (key.compareTo((T) e) >= 0)
                break;
            es[k] = e;
            k = parent;
        }
        es[k] = key;
    }
poll方法，取出并删除队列首元素。维护二叉平衡堆时，删除的过程比较复杂，需要比较左右孩子哪个更小哪个就做父节点，依次向下操作，直到倒数第二层堆，由于不仅访问父节点，还有需要访问左右孩子，导致时间复杂度为O(logN)
    private static <T> void siftDownComparable(int k, T x, Object[] es, int n) {
        // assert n > 0;
        Comparable<? super T> key = (Comparable<? super T>)x;
        int half = n >>> 1;           // loop while a non-leaf
        while (k < half) {
            int child = (k << 1) + 1; // assume left child is least
            Object c = es[child];
            int right = child + 1;
            if (right < n &&
                ((Comparable<? super T>) c).compareTo((T) es[right]) > 0)
                c = es[child = right];
            if (key.compareTo((T) c) <= 0)
                break;
            es[k] = c;
            k = child;
        }
        es[k] = key;
    }