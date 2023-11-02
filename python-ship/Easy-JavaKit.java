PImage img;
int diameter;
int xcoord;
int ycoord;

//background
void setup(){
    size(800,475);
    img = loadImage("space_background.jpeg");

    background(0);
    image(img,0,0);
    
    //stars
    fill(255, 255, 255);
    for(int i = 0; i < 50; i++){
        diameter = int(random(0, 10));
        xcoord = int(random(0, 800));
        ycoord = int(random(0, 475));
        ellipse(xcoord, ycoord, diameter, diameter);
    }
        
    //sun
    fill(245, 130, 70);
    ellipse(0,250,150,150);

    //mercury
    fill(160, 150, 95);
    ellipse(155,310,50,50);
    
    //venus
    fill(175, 115, 70);
    ellipse(164,190,50,50);

    //earth
    fill(10, 165, 100);
    ellipse(170,250,50,50);
    
    //mars
    fill(215, 5, 5);
    ellipse(180,375,50,50);
    
    //jupiter
    fill(245, 180, 125);
    ellipse(260,350,50,50);

    //saturn
    fill(240, 230, 140);
    ellipse(350,250,50,50);
    
    //uranus
    fill(140, 255, 255);
    ellipse(540,350,50,50);
    
    //neptune
    fill(110, 120, 250);
    ellipse(790,250,50,50);
}

