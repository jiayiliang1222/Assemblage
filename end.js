let ribbons = [];
let stars = [];

function setup() {
    let canvas = createCanvas(windowWidth, windowHeight);
    canvas.id("p5-canvas");
    canvas.parent("p5-canvas-container");
    for (let i = 0; i < 100; i++) {
        let p = new Ribbon(width / 2, height / 2, random(10, 20), random(0.01, 0.03));
        ribbons.push(p);
    }

    for (let i = 0; i < 800; i++) {
        stars.push(
            new Particle(random(windowWidth / 3, windowWidth * 2 / 3), windowHeight, random(2, 5)));
    }
}

function draw() {
    background(34, 40, 49, 30);

    for (let i = 0; i < stars.length; i++) {
        let s = stars[i];
        s.move();
        s.reappear();
        s.display();
    }

    push();
    textAlign(CENTER);
    textFont("Times New Roman");
    push();
    fill(212, 200, 167);
    textSize(20);
    text("The Tarot Reading is Just for Fun.", width / 2, height / 2 - 15);
    text("Destiny is in Our Own Hands.", width / 2, height / 2 + 15);
    noFill();
    stroke(212, 200, 167);
    strokeWeight(3);
    rectMode(CENTER);
    rect(width / 2, height / 2, 350, 200);
    pop();

    for (let i = 0; i < ribbons.length; i++) {
        let p = ribbons[i];
        p.move();
        p.fall();
        p.display();
    }
}

class Ribbon {
    constructor(x, y, s, rSpd) {
        this.x = x;
        this.y = y;
        this.xSpd = random(-1, 1);
        this.ySpd = random(-8, -5);
        this.size = s;
        this.rotSpd = rSpd;
    }
    move() {
        this.x += this.xSpd;
        this.y += this.ySpd;
    }
    fall() {
        this.ySpd += 0.1;
    }
    display() {
        push();
        stroke(212, 200, 167);
        strokeWeight(3);
        translate(this.x, this.y);
        rotate(frameCount * this.rotSpd);
        rectMode(CENTER);
        rect(0, 0, this.size, this.size / 2);
        pop();
    }
}

class Particle {
    constructor(x, y, dia) {
        this.x = x;
        this.y = y;
        this.dia = dia;
        this.xSpd = random(-1, 1);
        this.ySpd = random(-1, 1);
        this.brightness = 255;
    }
    move() {
        this.x += this.xSpd;
        this.y -= this.ySpd;
    }
    reappear() {
        if (this.y < 0) {
            this.y = height;
        }
        if (this.y > height) {
            this.y = 0;
        }
        if (this.x < 0) {
            this.x = width;
        }
        if (this.x > width) {
            this.y = 0;
        }

    }
    display() {
        push();
        noStroke();

        fill(212, 200, 167, 10);
        ellipse(this.x, this.y, this.dia, this.dia);
        ellipse(this.x, this.y, this.dia / 2, this.dia / 2);
        pop();
    }
}