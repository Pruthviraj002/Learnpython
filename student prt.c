#include<stdio.h>
void main()
{
	int roll_number,sum;
	int english,phy,maths,electronic,cs;
	char name;
	float marks,average;
	
	printf("\n enter student roll_number:");
	scanf("\n%d",&roll_number);
	
	printf("\n enter student name:");
	scanf("%s",&name);
	
	printf("\n enter student mark in english: ");
	scanf("%d",&english);
	
	printf("\n enter student mark in phy: ");
	scanf("%d",&phy);
	
	printf("\n enter student mark in maths: ");
	scanf("%d",&maths);
	
	printf("\n enter student mark in electronic: ");
	scanf("%d",&electronic);
	
	printf("\n enter student mark in cs: ");
	scanf("%d",&cs);
	
	
	sum=english+phy+maths+electronic+cs;
	average=sum/5;
	printf("\n total marks=%d",sum);
	printf("\n average=%.2f",average);
}
