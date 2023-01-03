import random
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    冒泡排序
    稳定性：稳定
    时间复杂度 ：最佳：O(n) ，最差：O(n2)， 平均：O(n2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    <p>
    算法步骤:
    （1）比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    （2）对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    （3）针对所有的元素重复以上的步骤，除了最后一个；
    （4）重复步骤 1~3，直到排序完成。
    """
    for i in range(len(arr)):
        flag = True
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                flag = False
        if flag:
            break
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """
    选择排序
    稳定性：不稳定
    时间复杂度 ：最佳：O(n2) ，最差：O(n2)， 平均：O(n2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    算法步骤:
    （1）首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    （2）再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    （3）重复第 2 步，直到所有元素均排序完毕。
    """
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    插入排序
    稳定性：稳定
    时间复杂度 ：最佳：O(n) ，最差：O(n2)， 平均：O(n2)
    空间复杂度 ：O(1)
    排序方式 ：In-place
    算法步骤：
    （1）从第一个元素开始，该元素可以认为已经被排序；
    （2）取出下一个元素，在已经排序的元素序列中从后向前扫描；
    （3）如果该元素（已排序）大于新元素，将该元素移到下一位置；
    （4）重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置；
    （5）将新元素插入到该位置后；
    （6）重复步骤 2~5。
    """
    for i in range(len(arr)):
        pass
    pass


def check_order(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            raise Exception('列表乱序')
    return arr


if __name__ == '__main__':
    arr = list(range(100))
    random.shuffle(arr)
    print(list(arr))

    # print(check_order(bubble_sort(arr)))
    # print(check_order(selection_sort(arr)))
    #
    # /**

    # */
    # public static int[] insertionSort(int[] arr) {
    # for (int i = 1; i < arr.length; i++) {
    #     int cur = arr[i];
    # int preIndex = i;
    # for (; preIndex >= 1 && arr[preIndex - 1] > cur; preIndex--) {
    # arr[preIndex] = arr[preIndex - 1];
    # }
    # arr[preIndex] = cur;
    # }
    # return arr;
    # }
    #
    # /**
    # * 希尔排序
    #   * 稳定性：不稳定
    #            * 时间复杂度 ：最佳：O(nlogn)， 最差：O(n2) 平均：O(nlogn)
    #                                                         * 空间复杂度 ：O(1)
    #                                                                       * 最差：O(n2)列子：5,1,6,2,7,3,8,4
    #                                                                                                      * 排序方式 ：In-place
    #                                                                                                                  * 算法步骤：
    # * （1）选择一个增量序列 {t1, t2, …, tk}，其中 (ti>tj, i<j, tk=1)；
    # * （2）按增量序列个数 k，对序列进行 k 趟排序；
    # * （3）每趟排序，根据对应的增量 t，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    # */
    # public static int[] shellSort(int[] arr) {
    # int incFactor = 2;
    # for (int gap = arr.length / incFactor; gap > 0; gap /= incFactor) {
    # for (int i = 1; i < arr.length; i++) {
    # int cur = arr[i];
    # int preIndex = i;
    # for (; preIndex >= gap && arr[preIndex - gap] > cur; preIndex -= gap) {
    # arr[preIndex] = arr[preIndex - gap];
    # }
    # arr[preIndex] = cur;
    # }
    # }
    # return arr;
    # }
    #
    # /**
    # * 归并排序
    #   * 稳定性：稳定
    #            * 时间复杂度 ：最佳：O(nlogn)， 最差：(nlogn) 平均：(nlogn)
    #                                                           * 空间复杂度 ：O(n)
    #                                                                         * 排序方式 ：Out-place
    #                                                                                     * 算法步骤：
    # * 归并排序算法是一个递归过程，边界条件为当输入序列仅有一个元素时，直接返回，具体过程如下：
    # * （1）如果输入内只有一个元素，则直接返回，否则将长度为 n 的输入序列分成两个长度为 n/2 的子序列；
    # * （2）分别对这两个子序列进行归并排序，使子序列变为有序状态；
    # * （3）设定两个指针，分别指向两个已经排序子序列的起始位置；
    # * （4）比较两个指针所指向的元素，选择相对小的元素放入到合并空间（用于存放排序结果），并移动指针到下一位置；
    # * （5）重复步骤 3 ~ 4 直到某一指针达到序列尾；
    # * （6）将另一序列剩下的所有元素直接复制到合并序列尾。
    # */
    # public static int[] mergeSort(int[] arr) {
    # if (arr.length <= 1) {
    # return arr;
    # }
    # int middle = arr.length / 2;
    # int[] arr1 = Arrays.copyOfRange(arr, 0, middle);
    # int[] arr2 = Arrays.copyOfRange(arr, middle, arr.length);
    # return merge(mergeSort(arr1), mergeSort(arr2));
    # }
    #
    # public static int[] merge(int[] arr1, int[] arr2) {
    # int[] sortArr = new int[arr1.length + arr2.length];
    # int index1 = 0, index2 = 0;
    # while (index1 < arr1.length && index2 < arr2.length) {
    # if (arr1[index1] <= arr2[index2]) {
    # sortArr[index1 + index2] = arr1[index1++];
    # } else {
    # sortArr[index1 + index2] = arr2[index2++];
    # }
    # }
    # if (index1 < arr1.length) {
    # System.arraycopy(arr1, index1, sortArr, index1 + index2, arr1.length - index1);
    # } else if (index2 < arr2.length) {
    # System.arraycopy(arr2, index2, sortArr, index1 + index2, arr2.length - index2);
    # }
    # return sortArr;
    # }
    #
    #
    # /**
    # * 快速排序
    #   * 稳定性：不稳定
    #            * 时间复杂度 ：最佳：O(nlogn)， 最差：O(nlogn)，平均：O(nlogn)
    #                                                            * 空间复杂度 ：O(nlogn)
    #                                                                          * 排序方式 ：In-place
    #                                                                                      * 算法步骤：
    # * 归并排序算法是一个递归过程，边界条件为当输入序列仅有一个元素时，直接返回，具体过程如下：
    # * （1）从序列中随机挑出一个元素，做为 “基准”(pivot)；
    # * （2）重新排列序列，将所有比基准值小的元素摆放在基准前面，所有比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个操作结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    # * （3）递归地把小于基准值元素的子序列和大于基准值元素的子序列进行快速排序。
    # */
    # public static void quickSort(int[] arr, int left, int right) {
    # if (left < right) {
    # int position = partition(arr, left, right);
    # quickSort(arr, left, position - 1);
    # quickSort(arr, position + 1, right);
    # }
    # }
    #
    # public static int partition(int[] arr, int left, int right) {
    # int pivot = arr[right];
    # int pointer = left;
    # for (int i = left; i < right; i++) {
    # if (arr[i] < pivot) {
    # swap(arr, i, pointer);
    # pointer++;
    # }
    # }
    # swap(arr, pointer, right);
    # return pointer;
    # }
    #
    # public static int[] quickSort(int[] arr) {
    # quickSort(arr, 0, arr.length - 1);
    # return arr;
    # }
    #
    # /**
    # * 堆排序 https://www.cnblogs.com/chengxiao/p/6129630.html
    #                                                      * 稳定性：不稳定
    #                                                               * 时间复杂度 ：最佳：O(nlogn)， 最差：O(nlogn)， 平均：O(nlogn)
    #                                                                                                                * 空间复杂度 ：1
    #                                                                                                                              * 排序方式 ：In-place
    #                                                                                                                                          * 算法步骤：
    # * （1）将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆
    #                             * （2）将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端
    #                                                                         * （3）重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序
    #                                                                                                                                                                   */
    #                                                                                                                                                                   public static int[] heapSort(int[] arr) {
    # //1.构建大顶堆
    # for (int i = arr.length / 2 - 1; i >= 0; i--) {
    #     adjustHeap(arr, i, arr.length); //从第一个非叶子结点从下至上，从右至左调整结构
    # }
    # //2.调整堆结构 & 交换堆顶元素与末尾元素
    # for (int i = arr.length - 1; i > 0; i--) {
    #     swap(arr, 0, i); //将堆顶元素与末尾元素进行交换
    # adjustHeap(arr, 0, i); //重新对堆进行调整
    # }
    # return arr;
    # }
    #
    # /**
    # * 调整大顶堆（仅是调整过程，建立在大顶堆已构建的基础上）
    # *
    # * @param arr    数组
    #                 * @param index  当前根节点
    #                                 * @param length 数组长度
    #                                                 */
    #                                                 public static void adjustHeap(int[] arr, int index, int length) {
    # int temp = arr[index]; //先取出当前元素index
    #
    # for (int child = index * 2 + 1; child < length; child = child * 2 + 1) { //从index结点的左子结点开始，也就是2i+1处开始
    # if (child + 1 < length && arr[child] < arr[child + 1]) { //如果左子结点小于右子结点，k指向右子结点
    # child++;
    # }
    # if (arr[child] > temp) { //如果子节点大于父节点，将子节点值赋给父节点（不用进行交换）
    # arr[index] = arr[child];
    # index = child;
    # } else {
    # break;
    # }
    # }
    # arr[index] = temp; //将temp值放到最终的位置
    # }
    #
    # /**
    # * 计数排序
    #   * 稳定性：稳定
    #            * 时间复杂度 ：最佳：O(n+k) 最差：O(n+k) 平均：O(n+k)
    #                                                       * 空间复杂度 ：O(k)
    #                                                                     * 排序方式 ：In-place
    #                                                                                 * 算法步骤：
    # * （1）找出数组中的最大值 max、最小值 min
    #                                    * （2）创建一个新数组 C，其长度是 max-min+1，其元素默认值都为 0
    #                                                                                              * （3）遍历原数组 A 中的元素 A[i]，以 A[i]-min 作为 C 数组的索引，以 A[i] 的值在 A 中元素出现次数作为 C[A[i]-min] 的值
    #                                                                                                                                                                                                            * （4）覆盖原来数组的值
    #                                                                                                                                                                                                                 */
    #                                                                                                                                                                                                                 public static int[] countingSort(int[] arr) {
    #     int[] minMax = getMinMax(arr);
    # int min = minMax[0];
    # int max = minMax[1];
    # int[] count = new int[max - min + 1];
    # for (int i : arr) {
    #     count[i - min]++;
    # }
    # int index = min;
    # for (int i = 0; i < arr.length; ) {
    # if (count[index - min]-- > 0) {
    # arr[i++] = index;
    # } else {
    # index++;
    # }
    # }
    # return arr;
    # }
    #
    # private static int[] getMinMax(int[] arr) {
    # if (arr == null || arr.length == 0) {
    # return arr;
    # }
    # int min = arr[0], max = arr[0];
    # for (int i : arr) {
    # if (i > max) {
    # max = i;
    # }
    # if (i < min) {
    # min = i;
    # }
    # }
    # return new int[]{min, max};
    # }
    #
    # /**
    # * 桶排序
    #   * 稳定性：稳定
    #            * 时间复杂度 ：最佳：O(n+k) 最差：O(n²) 平均：O(n+k)
    #                                                      * 空间复杂度 ：O(k)
    #                                                                    * 排序方式 ：Out-place
    #                                                                                * 算法步骤：
    # * （1）设置一个 BucketSize，作为每个桶所能放置多少个不同数值；
    # * （2）遍历输入数据，并且把数据依次映射到对应的桶里去；
    # * （3）对每个非空的桶进行排序，可以使用其它排序方法，也可以递归使用桶排序；
    # */
    # public static int[] bucketSort(int[] arr) {
    # int[] minMax = getMinMax(arr);
    # int min = minMax[0];
    # int max = minMax[1];
    #
    # int bucketCount =
    # (max - min) / arr.length + 1;
    # List<List<Integer>> list = new ArrayList<>();
    #
    # for (int i = 0; i < bucketCount; i++) {
    #     list.add(new ArrayList<>());
    # }
    #
    # for (int i : arr) {
    #     list.get((i - min) % bucketCount).add(i);
    # }
    # list.forEach(item -> {
    # if (item.size() > 0) {
    #     item.sort(null);
    # }
    # });
    # return list.stream().flatMap(Collection::stream).mapToInt(Integer::intValue).toArray();
    # }
    #
    # /**
    # * 桶排序
    #   * 稳定性：稳定
    #            * 时间复杂度 ：最佳：O(n×k) 最差：O(n×k) 平均：O(n×k)
    # * 空间复杂度 ：O(n+k)
    #               * 排序方式 ：Out-place
    #                           * 算法步骤：
    # * （1）取得数组中的最大数，并取得位数，即为迭代次数 N（例如：数组中最大数值为 1000，则 N=4）；
    # * （2）A 为原始数组，从最低位开始取每个位组成 radix 数组；
    # * （3）对 radix 进行计数排序（利用计数排序适用于小范围数的特点）；
    # * （4）将 radix 依次赋值给原数组；
    # */
    # public static int[] radixSort(int[] arr) {
    # if (arr == null || arr.length < 2) {
    # return arr;
    # }
    # int max = getMinMax(arr)[1];
    # int count = 1;
    # while (max / 10 > 0) {
    # max /= 10;
    # count++;
    # }
    # for (int i = 0; i < count; i++) {
    #     List<List<Integer>> lists = new ArrayList<>();
    # for (int j = 0; j < 10; j++) {
    # lists.add(new ArrayList<>());
    # }
    # for (int data : arr) {
    #     lists.get(data / (int) Math.pow(10, i) % 10).add(data);
    # }
    # int index = 0;
    # for (List<Integer> list : lists) {
    # for (Integer integer : list) {
    #     arr[index++] = integer;
    # }
    # }
    # }
    # return arr;
    # }
    #
    #
