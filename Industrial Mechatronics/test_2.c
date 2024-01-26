#include <stdio.h>
#include <string.h>
 
struct Student 
{
    char first_name[50];
    char last_name[50];
    char university[100];
    char faculty[100];
    int year;

};

void Student_data(struct Student student, int i);
void printStudent(struct Student student);

int main() 
{
    struct Student Student;
    int number_of_students;

    printf("How many students are going to register their data? ");
    scanf("%d", &number_of_students);

    for(int i=1;i<=number_of_students;i++)
    {
        Student_data(Student, i);
    }
    return 0;
}

void Student_data(struct Student student, int i)
{
    printf("\nStudent # %d\n",i);

    printf( "Enter your first name: ");
    scanf("%s", student.first_name);

    printf( "Enter your last name: ");
    scanf("%s", student.last_name);

    printf("Enter the name of your university: ");
    scanf(" %49[^\n]", student.university);

    printf("Enter the name of your faculty: ");
    scanf(" %49[^\n]", student.faculty);

    printf( "Enter the year you enrolled %s: ",student.university);
    scanf("%d", &student.year);

    printStudent(student);
}

void printStudent(struct Student student) 
{
    printf( "\nStudent name : %s %s\n", student.first_name, student.last_name);
    printf( "Univeristy : %s\n", student.university);
    printf( "Faculty : %s\n", student.faculty);
    printf( "Enrollment year : %d\n", student.year);
}
