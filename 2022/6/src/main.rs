#![feature(test)]
mod test;

use std::{
    io::Read,
    fs::File, str::Chars,
};

fn main() {
    // get command line argument
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 3 {
        panic!("Usage: {} -p <1|2>", args[0]);
    }
    let part = &args[2];

    let mut file = File::open("streams.txt").expect("file not found");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("something went wrong reading the file");

    let chars = contents.chars();

    match str::parse::<u8>(part).unwrap() {
        1 => find_marker(4, &chars),
        2 => find_marker(14, &chars),
        _ => panic!("Invalid part number"),
    };
}

fn find_marker(marker_len: usize, chars: &Chars) -> usize {
    let mut chars = chars.clone();

    // load the first 3 chars
    let mut window = (0..marker_len - 1).map(|_| chars.next().unwrap()).collect::<Vec<char>>();

    let mut marker = marker_len - 1;

    while let Some(c) = chars.next() {
        marker += 1;

        // load the next char
        window.push(c);

        // check that all characters are different from each other
        if check_unique(&window) {
            println!("{}: {:?}", marker, window);
            break;
        }

        // remove the first char
        window.remove(0);
    }

    marker
}

fn check_unique(char_set: &Vec<char>) -> bool {
    let mut mask = 0i32;

    for c in char_set {
        let bit = 1 << (*c as u8 - 'a' as u8);
        if mask & bit != 0 {
            return false;
        }

        mask |= bit;
    }

    true
}