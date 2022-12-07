#[cfg(test)]
mod tests {
    extern crate test;
    use super::*;
    use test::Bencher;
    use crate::find_marker;
    use std::{
        io::Read,
        fs::File,
    };

    #[bench]
    fn bench_rep_4(b: &mut Bencher) {
        b.iter(|| {
            test::black_box({
                let mut file = File::open("streams.txt").expect("file not found");
                let mut contents = String::new();
                file.read_to_string(&mut contents).expect("something went wrong reading the file");
                let mut chars = contents.chars();
                find_marker(4, &chars)
            });
        })
    }
    
    #[bench]
    fn bench_rep_14(b: &mut Bencher) {
        b.iter(|| {
            test::black_box({
                let mut file = File::open("streams.txt").expect("file not found");
                let mut contents = String::new();
                file.read_to_string(&mut contents).expect("something went wrong reading the file");
                let mut chars = contents.chars();
                find_marker(14, &chars)
            });
        })
    }
    
    #[bench]
    fn bench_rep_4_pre_read_file(b: &mut Bencher) {
        let mut file = File::open("streams.txt").expect("file not found");
        let mut contents = String::new();
        file.read_to_string(&mut contents).expect("something went wrong reading the file");
        let mut chars = contents.chars();
    
        b.iter(|| {
            test::black_box(find_marker(4, &chars));
        })
    }
    
    #[bench]
    fn bench_rep_14_pre_read_file(b: &mut Bencher) {
        let mut file = File::open("streams.txt").expect("file not found");
        let mut contents = String::new();
        file.read_to_string(&mut contents).expect("something went wrong reading the file");
        let mut chars = contents.chars();
    
        b.iter(|| {
            test::black_box(find_marker(14, &chars));
        })
    }
}