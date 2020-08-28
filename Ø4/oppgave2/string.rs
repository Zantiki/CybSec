

fn string_modifier(mut in_string_: String) -> String{

    let to_find = ['&', '<', '>'];
    let replacement = ["&amp", "&lt", "&gt"];
    println!("String before modification: {}", in_string_);
    for i in 0..3 {
        in_string_ = in_string_.replace(to_find[i], replacement[i]);
    }
    println!("String after modification: {}", in_string_);
    return in_string_;

}

fn main() {
    let in_string: String = "&&&<<<>>>>>>".to_string();
    string_modifier(in_string);
}
