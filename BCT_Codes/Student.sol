// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract StudentData {

    // Define a structure to hold student information
    struct Student {
        uint256 id;
        string name;
        uint8 age;
    }

    // Array to store list of students
    Student[] public students;

    // Function to add a new student
    function addStudent(uint256 _id, string memory _name, uint8 _age) public {
        students.push(Student(_id, _name, _age));
    }

    // Function to get the details of a student by index
    function getStudent(uint256 index) public view returns (uint256, string memory, uint8) {
        require(index < students.length, "Invalid index.");
        Student memory student = students[index];
        return (student.id, student.name, student.age);
    }

     // Receive function to handle plain Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed.");
    }

    // Fallback function to handle unknown function calls or Ether sent with data
    fallback() external payable {
        revert("Fallback function called. No direct payments allowed.");
    }

    // Function to get total number of students (optional)
    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }
}
