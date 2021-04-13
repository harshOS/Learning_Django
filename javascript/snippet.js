phone = {
    brand : 'Xiaomi',
    model : 'Note 7 pro',
    price : 14999,
    colour : 'black',
    fullName : function() {
        return this.brand+ " " + this.model;
    }

}

console.log(phone.brand)
console.log(phone.fullName())
console.log(phone.price)