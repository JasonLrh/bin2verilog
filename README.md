# a tool covey bin file to Verilog ROM

This is a python tool 

~~~shell
python3 bin2v.py -b sim.bin -o RAM.v -addr_width 32 -data_width 8
~~~

~~~verilog
`timescale 1ns / 1ps

module ROM(
	input clk,
    input [31:0] addr,
    output reg [7:0] data
);

always@(*)
    case (addr)
		31'h00000000: data=7'h75
		31'h00000001: data=7'h70
		31'h00000002: data=7'h03
		31'h00000003: data=7'h75
        // ......
		31'h00000022: data=7'h50
		31'h00000023: data=7'h8E
		31'h00000024: data=7'h60
		31'h00000025: data=7'h80
		31'h00000026: data=7'hFE

        default: data = 8'h00;
    endcase
endmodule

~~~

use it well