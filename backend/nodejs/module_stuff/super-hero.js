class SuperHero {
    constructor (name) {
        this.name = name;
    };

    getName(){
        return this.name;
    };

    setName(name){
        this.name = name;
    };

}

module.exports = SuperHero;