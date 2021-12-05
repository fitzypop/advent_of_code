const FILE_NAME: &str = "../data.txt";

fn main() {
    let data = read_data_file(FILE_NAME);
    println!("Puzzle 1 answer is: {}", compute_increase(&data));
    println!("Puzzle 2 answer is: {}",chunk_and_compute(&data));

}

fn read_data_file(file_name: &str) -> Vec<u32> {
    std::fs::read_to_string(file_name)
        .unwrap()
        .lines()
        .filter_map(|x|  x.parse::<u32>().ok())
        .collect()
}

fn compute_increase(data: &Vec<u32>) -> u32 {
    let mut increase_counter = 0;

    for i in 1..data.len() {
        if data[i] > data[i -1] {
            increase_counter += 1;
        }
    }

    increase_counter
}

fn chunk_and_compute(data: &Vec<u32>) -> u32 {
    let mut chunks: Vec<u32> = vec![];

    for i in 0..data.len() - 2 {
        let sum = data[i] + data[i+1] + data[i+2];
        chunks.push(sum);
    }

    compute_increase(&chunks)
}
