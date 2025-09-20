fn binary_search(arr: Vec<i32>, target: i32) -> bool {
    let mut start = 0;
    let mut end = arr.len() as i32 - 1;
    while start <= end {
        let mut mid = start + (end - start) / 2;
        let mid_val = arr[mid as usize];
        if mid_val == target {
            return true;
        } else if mid_val > target {
            end = mid - 1;
        } else if mid_val < target {
            start = mid + 1;
        }
    }
    false
}

fn main() {
    let tests: Vec<(Vec<i32>, i32, bool)> = vec![
        (vec![], 3, false),
        (vec![1], 1, true),
        (vec![1], 2, false),
        (vec![1, 2, 3, 4, 5], 3, true),
        (vec![1, 2, 3, 4, 5], 1, true),
        (vec![1, 2, 3, 4, 5], 5, true),
        (vec![1, 2, 3, 4, 5], 6, false),
        (vec![1, 2, 3, 4, 5], 0, false),
        (vec![1, 1, 1, 1], 1, true),
        (vec![1, 2, 4, 8, 16, 32], 15, false),
    ];

    for (i, (arr, target, expected)) in tests.into_iter().enumerate() {
        let result = binary_search(arr.clone(), target);
        println!(
            "Test {} -> search {:?} for {}: got {}, expected {}",
            i + 1,
            arr,
            target,
            result,
            expected
        );
    }
}
