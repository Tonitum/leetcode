use std::collections::HashMap;

fn has_two_sum(target: i32, nums: Vec<i32>) -> Vec<i32> {
    let mut complements: HashMap<i32, usize> = HashMap::new();
    // start a loop
    for i in 0..nums.len() {
        // get the current value
        let current_value = nums.get(i).unwrap();
        // calculate the complement (target - current)
        let difference = target - current_value;
        // check a hashmap for the complement (which holds the index of that value)
        let complement = complements.get(&difference);
        // if the complement is there, return the current index and the index of the complement
        if complement.is_some() {
            return [
                complement.unwrap().to_owned().try_into().unwrap(),
                i.try_into().unwrap(),
            ]
            .to_vec();
        }
        // if not, add the current value to the hashmap, key = current value, value = index
        complements.insert(*current_value, i);
    }
    // this is O(n+1) time (so O(n), since constants go away), since we iterate through the loop
    // once and then do a hash map lookup (which is constant time)
    return [-1, -1].to_vec();
}

fn main() {
    let input = [2, 7, 11, 15].to_vec();
    let target = 9;
    let res = has_two_sum(target, input);
    println!("{:?}", res);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        let input = [2, 7, 11, 15].to_vec();
        let target = 9;
        let res = has_two_sum(target, input);
        assert_eq!(res[0], 0);
        assert_eq!(res[1], 1);
    }
    #[test]
    fn test_case_2() {
        let input = [3, 2, 4].to_vec();
        let target = 6;
        let res = has_two_sum(target, input);
        assert_eq!(res[0], 1);
        assert_eq!(res[1], 2);
    }
    #[test]
    fn test_case_3() {
        let input = [3, 3].to_vec();
        let target = 6;
        let res = has_two_sum(target, input);
        assert_eq!(res[0], 0);
        assert_eq!(res[1], 1);
    }
}
