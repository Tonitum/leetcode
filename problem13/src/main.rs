fn roman_to_integer(roman_numerals: &str) -> i32 {
    // convert the given roman numerals to an integer
    // Approach one:
    // use a hash map to count the number of symbols
    // start from the back of the string, we count all of the I's
    // we then know that any I that comes later must be subtracted from the corresponding larger
    // number that comes after it. same thing for V, X, L etc.
    let mut value = 0;
    let mut next_start = 0;
    for i in (next_start..roman_numerals.len().try_into().expect("")).rev() {
        let c = roman_numerals.chars().nth(i).unwrap();
        if c != 'I' {
            next_start = i;
            break;
        }
        value += 1;
    }
    return value;
}


fn main() {
    println!("{}", roman_to_integer(&"III".to_string()));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        assert_eq!(roman_to_integer(&"III".to_string()), 3);
    }

    #[test]
    fn test_case_2() {
        assert_eq!(roman_to_integer(&"LVIII".to_string()), 58);
    }
}
