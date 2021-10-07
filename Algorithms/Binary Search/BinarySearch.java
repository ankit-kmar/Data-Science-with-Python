//TWO SUM II - INPUT ARRAY IS SORTED.

/* Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.*/

/* Return the indices of the two numbers, index1 and index2,
as an integer array [index1, index2] of length 2.*/

public class BinarySearch {
    public static void main(String[] args) {
        int[] num = {2, 3, 4};
        int target = 6;
        System.out.println(findNum(num, target));
    }
    static int[] findNum(int[] numbers, int target)
    {
        int start = 0;
        int end = numbers.length - 1;
        while(start <= end)
        {
            int mid = start + (end - start)/2;
            if(numbers[start] + numbers[end] == target)
            {
                break;
            }
            else if(target > numbers[mid])
            {
                end = mid;
            }
            else
            {
                start = mid + 1;
            }
        }
        return new int[]{++start, ++end};
    }
}
