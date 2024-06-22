a="'string literilas\
     character literial\
         numeriacl\
                Boolen\
                 Literial collection\
                   Special literial'";
print(a);

single='hai';
double="to"
triple='''all my frinds
how are you ?''';
multi="what\'s your name:";
print(single,double,triple,multi);


x=0b1001; #binary Literials
y=1234458794856798569;#decimal Literial
z=0o1237653421;#octal literial
u=0x12def;
print(x);
print(y);
print(z);
print(u);


f1=1/2.5e62;
f2=100.5;    #folat Literial
print(f1,f2);

c=2+8j;                       #complmex Literial
print(c,c.imag,c.real)

x=(1==True);
y=(0==False);
z=(3==True);       #boolean Literials
u=True+10;
v=False+10;
print(x,y,z,u,v);

var=11;
var2=None;    #Special Literials
print(var,var2);

Literial Colletions

list1=[1,"hai",2.3];
print(list1);         List colletion Literials
print(list1+[2,3,4,5]);

tuple1=(1,2,"hai",[5,6]);
print(tuple1);                    tuple Colletion Literials 
 
dic={2:3,"hai":"bye"};            Dictionary colletion Literials
print(dic); 

se1={1,1,2,3,3,210};           Set colletion Literials
se2={2,5,4}
print(se1.union(se2));
print(se1);
