%Convert files

formatSp = '%f %f';
sizeA = [2 Inf];

fileI = fopen('linF-250us-5MSps-153p5cm01.asc','r');
AI = fscanf(fileI,formatSp,sizeA);
fclose(fileI);
AI=AI';

fileQ = fopen('linF-250us-5MSps-153p5cm02.asc','r');
AQ = fscanf(fileQ,formatSp,sizeA);
fclose(fileQ);
AQ=AQ';

t1 = (AI(:,1))';
Q1 = (AQ(:,2))';
I1 = (AI(:,2))';
%t = t1(5200:15200);
%Q = Q1(5200:15200);
%I = I1(5200:15200);
t = t1(2700:5200);
Q = Q1(2700:5200);
I = I1(2700:5200);

A = [t; Q; I];

file3 = fopen('linF-250us-5MSps-153p5cm.txt','wt');
for i = 1:size(A,1)
    fprintf(file3,'%g\t',A(i,:));
    fprintf(file3,'\n');
end
fclose(file3);
%}
