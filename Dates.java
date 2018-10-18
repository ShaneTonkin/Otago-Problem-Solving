/** Shane Tonkin - 2791399 - Etude 5
  * This program checks the format of dates from
  * stdin. If the date is in the incorrect format the 
  * program will return why the format is incorrect.
  */
import java.util.Scanner;
import java.lang.String;
import java.lang.Character;
import java.lang.Integer;

public class Dates{
  
  /** This method checks the format of one date
    * and prints why the date is incorrect to console
    * @param String date : the date for format checking
    */ 
  static void checkFormat(String date){
    String dateString = date;
    int seperatorIndex = 0;
    int firstSep = 0;
    int secondSep = 0;
    int otherSeperatorIndex = 0;
    boolean validSeperators = false;
    char seperator = ' ';
    String day = " ";
    String month = " ";
    String year = " ";   
    boolean isFeb = false;
    int maxDay = 31;
    
    if(date.length()<6){
      System.out.println(date + " : INVALID DATE : use the format dd/mm/yyyy");
      return;
    }
    //Find the seperators and make sure they are the same
    for(char c : date.substring(0,3).toCharArray()){
      if(Character.isWhitespace(c)||c == '-' || c == '/' ){
        seperator = c;
        firstSep = seperatorIndex;
      }
      seperatorIndex++;
    }
    if(firstSep == 0){
      if(Character.isDigit(date.toCharArray()[2])){
        System.out.println(date + " : INVALID DAY : use the format dd/mm/yyyy");
        return;
      }
      System.out.println(date + " : INVALID SEPERATORS : use the format dd/mm/yyyy");
      return;
    }
    for(char c : date.substring(seperatorIndex,date.length()).toCharArray()){
      if(c == seperator){
        otherSeperatorIndex = seperatorIndex;
        validSeperators =true;
        secondSep = seperatorIndex;
        break;
      }
      seperatorIndex++;
    }
    if(!validSeperators){
      System.out.println(dateString + " : INVALID SEPERATORS");
      System.out.print(": Try using the same one and from these seperators ( SPACE or / or - )\n");
      return;
    }
    
    //Split the String into the 3 features based upon the seperators
    day = dateString.substring(0,firstSep);
    month = dateString.substring(firstSep+1,secondSep);
    year = dateString.substring(secondSep+1,date.length());
    
    if(day.contains(" ") || day.contains("-") || day.contains("/")){
      System.out.println(date + " : INVALID SEPERATORS : Too many");
      return;
    }
      if(month.contains(" ") || month.contains("-") || month.contains("/")){
      System.out.println(date + " : INVALID SEPERATORS : Too many");
      return;
    }
       if(year.contains(" ") || year.contains("-") || year.contains("/")){
      System.out.println(date + " : INVALID SEPERATORS : Too many");
      return;
    }
    //check if day is all ints
    if(!day.matches("[0-9]+")){
      System.out.println(date + " : INVALID DAY");
      return;
    }
    //check if year is all ints
    if(year.matches("[0-9]+")){
      if(year.length() == 4){
        //check if it is in the time range
        if(Integer.parseInt(year) < 1752 || Integer.parseInt(year) > 3000){
          System.out.println(date + " : INVALID YEAR : Date out of range 1753 - 3000");
          return;
        }
      }else if(year.length() == 2){
        //convert to 4 digits for easier leap year checking
        if(Integer.parseInt(year) < 51){
          //add 2000 to the date
          year = "20" + year;
        }else{
          //add 1900 to the date
          year = "19"+year;
        }
      }else{
        System.out.println(date + " : INVALID YEAR");
        return;
      }
    }else{
      System.out.println(date + " : INVALID YEAR");
      return;
    }
    //check for leap year
    if(Integer.parseInt(year) % 4 == 0){
      //no idea
    }
    //check month
    if(month.length()>3){
      System.out.println(date + " : INVALID MONTH : enter the first 3 letters"); 
      return;
    }else{
      //if month is in STRING form
      //find the largest possible value the day could be
      if(month.equals("Jan")||month.equals("jan")||month.equals("JAN")||month.equals("01")||month.equals("1")){
        maxDay = 31;
        month = "Jan";
      }else if(month.equals("Feb")||month.equals("feb")||month.equals("FEB")||month.equals("02")||month.equals("2")){
        maxDay = 28;
        month = "Feb";
        isFeb = true;
      }else if(month.equals("Mar")||month.equals("mar")||month.equals("Mar")||month.equals("03")||month.equals("3")){
        maxDay = 31;
        month = "Apr";
      }else if(month.equals("Apr")||month.equals("apr")||month.equals("APR")||month.equals("04")||month.equals("4")){
        maxDay = 30;
        month = "Mar";
      }else if(month.equals("May")||month.equals("may")||month.equals("MAY")||month.equals("05")||month.equals("5")){
        maxDay = 31;
        month = "May";
      }else if(month.equals("Jun")||month.equals("jun")||month.equals("JUN")||month.equals("06")||month.equals("6")){
        maxDay = 30;
        month = "Jun";
      }else if(month.equals("Jul")||month.equals("jul")||month.equals("JUL")||month.equals("07")||month.equals("7")){
        maxDay = 31;
        month = "Jul";
      }else if(month.equals("Aug")||month.equals("aug")||month.equals("AUG")||month.equals("08")||month.equals("8")){
        maxDay = 31;
        month = "Aug";
      }else if(month.equals("Sep")||month.equals("sep")||month.equals("SEP")||month.equals("09")||month.equals("9")){
        maxDay = 30;
        month = "Sep";
      }else if(month.equals("Oct")||month.equals("oct")||month.equals("OCT")||month.equals("10")||month.equals("10")){
        maxDay = 31;
        month = "Oct";
      }else if(month.equals("Nov")||month.equals("nov")||month.equals("NOV")||month.equals("11")||month.equals("11")){
        maxDay = 30;
        month = "Nov";
      }else if(month.equals("Dec")||month.equals("dec")||month.equals("DEC")||month.equals("12")||month.equals("12")){
        maxDay = 31;
        month = "Dec";
      }else{
        System.out.println(date + " : INVALID MONTH");
        return;
      }
    }
    //Check for a leap year if nessecary 
    if(isFeb){
      if(Integer.parseInt(year) % 4 == 0){
        if(Integer.parseInt(year) % 100 == 0){
          if(Integer.parseInt(year) % 400 != 0){
             maxDay -= 1;  
          }
        }
        maxDay += 1;
      }
    }
    //Check the day is within range
    if(Integer.parseInt(day)> maxDay || Integer.parseInt(day) < 1){
      System.out.println(date + " : INVALID DAY");
      return;
    }
    if(day.length() < 2){
      day = "0" + day;
    }
    //Test stuff
    System.out.println(day +" "+ month + " "+ year);
  }
  
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    String date = "";
    while(sc.hasNextLine()){
      checkFormat(sc.nextLine());
    }
    sc.close();
  }
}