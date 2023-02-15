#include <stdint.h>

__declspec(dllexport) uint8_t get_byte(uint8_t x[3])
{
    return x[0] << 6 | (0b11 & x[1]) << 4 | (0b11 & x[2]) << 2 | (0b11 & x[3]);
}