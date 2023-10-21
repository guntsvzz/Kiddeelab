-- create function
local function compare(a,b)
    if a > b then
        print('a is more than b')
    else if b < a then
        print('b is more than b')
    else 
        print('a is equal b')
    end
end

local ant = 5
local bat = 6
-- calling function
compare(ant, bat)