"use strict";
console.log("hello world, this is a test");
class Furry {
    constructor(name, species, noise) {
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
//# sourceMappingURL=test.js.map