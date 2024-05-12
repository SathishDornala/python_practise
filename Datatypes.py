#numeric Datatypes
a=3;
b="hai my friends";
c=3.500000;
d=3+7j;
print(a,type(a));
print(b,type(b));
print(c,type(c));
print(d,type(d));

print(isinstance(1+3j,complex));
print(isinstance(1,int));
print(isinstance(3.4,float));
print(isinstance("sathish",int));


a="sathish";
b="""sathish""";
c="'sathish'";
print(a,type(a));
print(b,type(b));
print(c,type(c));    

x="Dornala";
y="Sathish";
z=x+y; #concatination
print(z);
print(z*2); #multiple
print(z[3:8]);#slicing
print(z[-6:-1]);#backslicing
print(z[4]);
print(z[::-1]);#reverse of string
print(z[0:10:2]);#sub_slicing
print(z[-1:-10:-1]);

a="sathish";
t=[1,"sathish",a[1:4],7.8,1+2j,range(0,5)];
print(t);
t=tuple[1,"sathish",a[1:4],7.8,1+2j,range(0,5)];

l=[1,"hai python",2.5];
print(type(l));
print(l);
print(l[0:3]);
print(isinstance(l,list));
m=[1+4j,"JAVA",[1,33,2]];
print(m*2);
print(l+m);
print(l[::-1]);
list1=list[1,3];
print(list1);
print(type(list1));
l1=[1,2,3,4];
print(l1);
print(isinstance(l1,list));
# print(type(l1));
a=[1,23,34,45];
l1=list(a);
print(l1,type(l1),isinstance(l1,list));


t1=(1,2,34,56);
print(t1,type(t1));
print(isinstance(t1,tuple));
a=(1,2,3,4);
_t1=tuple(a);
print(_t1,type(_t1));
print(isinstance(_t1,tuple));

t_1=(1,2,3,4,5,6,7,8,90,0);
t_2=(0,9,8,7);
print(t_1+t_2);
print(t_2*2,"\t",t_1[5],"\t",t_1[::-1],"\t",t_1[0:5],"\t",t_1[::2],"\t",t_1[-1:-9:-2]);



dic={1:2,"a":4.5,"hai":[3,5]};
print(dic,type(dic),isinstance(dic,dict));
print(dic[1]);
print(dic["a"]);
print(dic.keys());
print(dic.items());

a=False;
print(a)
b=True;
print(b);
c=True;
print(c);
print(type(a),type(b),type(c));


a=1.7;b=7.5;c=8.4;
print(type(a));
print(type(b));
print(type(c));

set1=set();
print(set1);
l1=list();
print(l1);
t1=tuple();
print(t1);
dic=dict();
print(dic);
print(type(set1));

set2={1,2,3,3,3,4,4,4,4,4,4,4,4,4,4},5,6;
print(set2);
set3={1,2.3,"hai"};
print(set3);
# print(set3[2]);                 #indexing not possible
set3.add(10);
set3.add(0.1);
set3.add("apple");
print((set3));
set3.remove(10);
print(set3);