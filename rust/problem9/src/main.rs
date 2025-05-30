fn is_palidrome(x: i32) -> bool {
    if (x < 0) || ((x % 10 == 0) && (x != 0)) {
        return false;
    }

    let mut x_dup = x;
    let mut numbers: Vec<i32> = Vec::new();
    loop {
        let remainder = x_dup % 10;
        if x_dup < 10 {
            numbers.push(x_dup);
            break;
        }
        numbers.push(remainder);
        x_dup = x_dup / 10;
    }
    let len: u32 = numbers.len().try_into().unwrap();
    let mut new_mod = 10_i32.pow(len - 1);
    let mut potential = 0;
    for i in 0..numbers.len() {
        potential = potential + new_mod * numbers.get(i).unwrap();
        new_mod = new_mod / 10;
    }

    return potential == x;
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        assert!(is_palidrome(121));
    }
    #[test]
    fn test_case_2() {
        assert!(!is_palidrome(-121));
    }
    #[test]
    fn test_case_3() {
        assert!(!is_palidrome(10));
    }
    #[test]
    fn test_case_4() {
        assert!(is_palidrome(0));
    }
    #[test]
    fn test_case_5() {
        assert!(is_palidrome(1));
    }
    #[test]
    fn test_case_6() {
        assert!(is_palidrome(1001));
    }
    #[test]
    fn test_case_7() {
        assert!(is_palidrome(1000000001));
    }
}
