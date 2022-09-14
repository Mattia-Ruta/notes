console.log("hello world, this is a test");

class Furry {
    public name: String;
    public species: String;
    public noise: String;

    constructor(name: String, species: String, noise: String) {
        this.name = name;
        this.species = species;
        this.noise = noise;
    }

    makeNoise() {
        console.log(this.noise);
    }
    static test() {
        console.log("test");
    }
}

const fen = new Furry("Fennec", "Fennec", "Bark");

fen.makeNoise();

interface Numbers {
    count?: number;
}

const Test:<Numbers> = (props: Numbers) => {
    return <p>{props.count}</p>;
}
