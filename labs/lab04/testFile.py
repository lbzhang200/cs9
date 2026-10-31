from Stack import Stack 
from lab04 import solveMaze 

def test_stack_empty():
    s = Stack() 
    assert s.isEmpty() == True 
    assert s.size() == 0 

def test_stack_push_peek_pop():
    s = Stack()
    s.push(1)
    s.push([1, 2,])
    assert s.size() == 2
    assert s.isEmpty() == False
    assert s.pop() == [2, 3]
    assert s.peek() == 1
    assert s.pop()== 1      
    assert s.isEmpty() == True 

def test_stack_lifo_order():
    s = Stack()
    for i in range(5):
        s.push(i)
    result = []
    while not s.isEmpty():
        result.append(s.pop())
    assert result == [4, 3, 2, 1, 0]



#solve maze tests 

def test_example():
    maze = [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', ' ', '+', ' ', ' ', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['+', ' ', '+', '+', ' ', '+'],
        ['+', ' ', ' ', ' ', ' ', '+'],
        ['+', '+', '+', '+', '+', '+']]
    assert solveMAze(maze, 4, 4) == True
    assert maze == [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', 8, '+', 11, 12, '+'],
        ['+', 7, 9, 10, '+', '+'],
        ['+', 6, '+', '+', 2, '+'],
        ['+', 5, 4, 3, 1, '+'],
        ['+', '+', '+', '+', '+', '+']]
 
 
def test_start_next_to_goal_north():
    maze = [
        ['+', 'G', '+'],
        ['+', ' ', '+'],
        ['+', '+', '+']]
    assert solveMaze(maze, 1, 1) == True
    assert maze == [
        ['+', 'G', '+'],
        ['+', 1, '+'],
        ['+', '+', '+']]
 
 
def test_goal_to_the_east():
    maze = [
        ['+', '+', '+', '+'],
        ['+', ' ', ' ', 'G'],
        ['+', '+', '+', '+']]
    assert solveMaze(maze, 1, 1) == True
    assert maze == [
        ['+', '+', '+', '+'],
        ['+', 1, 2, 'G'],
        ['+', '+', '+', '+']]
 
 
def test_goal_to_the_south():
    maze = [
        ['+', '+', '+'],
        ['+', ' ', '+'],
        ['+', ' ', '+'],
        ['+', 'G', '+']]
    assert solveMaze(maze, 1, 1) == True
    assert maze == [
        ['+', '+', '+'],
        ['+', 1, '+'],
        ['+', 2, '+'],
        ['+', 'G', '+']]
 
 
def test_goal_to_the_west():
    maze = [
        ['+', '+', '+', '+'],
        ['G', ' ', ' ', '+'],
        ['+', '+', '+', '+']]
    assert solveMaze(maze, 1, 2) == True
    assert maze == [
        ['+', '+', '+', '+'],
        ['G', 2, 1, '+'],
        ['+', '+', '+', '+']]
 
 
def test_no_path():
    maze = [
        ['+', '+', '+', '+', '+'],
        ['+', ' ', '+', ' ', 'G'],
        ['+', ' ', '+', ' ', '+'],
        ['+', '+', '+', '+', '+']]
    assert solveMaze(maze, 1, 1) == False
    assert maze == [
        ['+', '+', '+', '+', '+'],
        ['+', 1, '+', ' ', 'G'],
        ['+', 2, '+', ' ', '+'],
        ['+', '+', '+', '+', '+']]
 
 
def test_no_path_single_cell():
    maze = [
        ['+', '+', '+'],
        ['+', ' ', '+'],
        ['+', '+', '+']]
    assert solveMaze(maze, 1, 1) == False
    assert maze == [
        ['+', '+', '+'],
        ['+', 1, '+'],
        ['+', '+', '+']]
 
 
def test_backtracking_dead_end():
    # Goes north into a dead end first, backtracks, then heads east to G
    maze = [
        ['+', '+', '+', '+', '+'],
        ['+', ' ', '+', '+', '+'],
        ['+', ' ', ' ', ' ', 'G'],
        ['+', '+', '+', '+', '+']]
    assert solveMaze(maze, 2, 1) == True
    assert maze == [
        ['+', '+', '+', '+', '+'],
        ['+', 2, '+', '+', '+'],
        ['+', 1, 3, 4, 'G'],
        ['+', '+', '+', '+', '+']]