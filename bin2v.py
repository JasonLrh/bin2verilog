import sys
import os
import argparse

parser = argparse.ArgumentParser(description='bin file to Verilog.v')
parser.add_argument('-b', help='Path to input [.bin] file', default='a.bin')
parser.add_argument('-o', help='Path to output [.v] file', default='ROM.v')
parser.add_argument('-addr_width', help='addr width', default=32)
parser.add_argument('-data_width', help='data width', default=8)

args = parser.parse_args()

with open(args.b, mode='rb') as input_bin_file:
    bin_content = input_bin_file.read()

if bin_content is None:
    print("! check input [.bin] file")
    exit(0)

with open(args.o, mode="w", encoding='utf-8') as output_v_file:
    if output_v_file.writable() == False:
        print("[.v] file can't write")
        exit(0)
    # write job
    output_v_file.write(
"""`timescale 1ns / 1ps

module ROM(
	input clk,
    input [%d:0] addr,
    output reg [%d:0] data
);

always@(*)
    case (addr)
"""%(args.addr_width - 1, args.data_width - 1))
    for i in range(len(bin_content)):
        output_v_file.write("\t\t%d"%(args.addr_width - 1) + "'h%08X:"%i + " data=%d"%(args.data_width - 1) + "'h%02X\n"%bin_content[i])
    output_v_file.write(
"""
        default: data = 8'h00;
    endcase
endmodule
"""
    )
    print("Write OK")