import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        MergeTwoSortedLists m = new MergeTwoSortedLists();

        int[] lt1 = new int[]{1,3,5};
        int[] lt2 = new int[]{1,2,5};
        ListNode l1 = new ListNode(0);
        ListNode l1c = l1;
        ListNode l2 = new ListNode(0);
        ListNode l2c = l2;
        for (int i :lt1) {
            l1c.next = new ListNode(i);
            l1c = l1c.next;
        }
        for (int i :lt2) {
            l2c.next = new ListNode(i);
            l2c = l2c.next;
        }
        ListNode l3 = m.mergeTwoLists(l1.next,l2.next);
        while (l3 != null) {
            System.out.println(l3.val);
            l3 = l3.next;
        }
    }
}
