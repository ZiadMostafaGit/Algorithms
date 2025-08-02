fn insertion_sort(arr: &mut [i32]) {
    let n = arr.len();
    //  let mut temp=0;
    let mut j = 1;
    for i in 0..n {
        j = i;
        while j != 0 && arr[j] < arr[j - 1] {
            // temp=arr[j-1];
            //   arr[j-1]=arr[j];
            //     arr[j]=temp;
            arr.swap(j, j - 1);
            j -= 1;
        }
    }
}

fn main() {
    let mut arr: [i32; 5];
    arr = [4, 7, 2, 5, 1];
    insertion_sort(&mut arr);
    println!("{:?}", arr);
}
