library ieee; -- 分号别忘了
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity tenAdd is
    port( clr, clk : in std_logic;
          cnt10: out std_logic_vector (3 downto 0)); -- 设置一个四位矢量
end tenAdd;

architecture one of tenAdd is
signal count: std_logic_vector (3 downto 0); -- 在process前定义一个局部变量 用于计数
begin
    process(clr,clk) -- 写入两个敏感信号
    begin
        if (clr = '1') then
                count <= "0000"; -- 0000 要用双引号
        elsif clk'event and clk = '1' then -- 高电平触发
            if (count < "1001") then
            count <= count + 1; -- 计数加1
           else
                count <= "0000"; -- 计数到9之后回到0000
           end if;
          end if;
          cnt10 <= count; -- 计数值赋给输出变量cnt10
    end process; -- 结束进程
end one; -- 结构体结束
