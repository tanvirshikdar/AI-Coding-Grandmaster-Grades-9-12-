import java.util.*;

class main {
  public static void main(String[] args) {
	int sum=0;
    String result;
    Scanner sc=new Scanner(System.in);
	System.out.println("Enter the number of Subjects: ");
	int noOfSubjects = sc.nextInt();
	int marks[]=new int[noOfSubjects]; 
	System.out.println("Enter the marks of " +noOfSubjects +" Subjects. Press Enter to give marks for another subject");
	for(int i=0;i<noOfSubjects;i++){
		marks[i]=sc.nextInt();
	}
	for(int j=0;j<noOfSubjects;j++){
		sum=sum+marks[j];
	}
	int percentage=sum/noOfSubjects;
	System.out.println(percentage);
	if(percentage>= 95){
		result="You scored O grade. Great Work!";

	}else if(percentage>90 && percentage<95){
		result="You scored A+.Well Done!";
	}
	else {
		result="you pased";
	}
	System.out.println(result);
  }
}