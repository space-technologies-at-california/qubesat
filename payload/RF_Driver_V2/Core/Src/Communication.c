/***************************************************************************//**
 *   @file   Communication.c
 *   @brief  Implementation of Communication Driver for RENESAS RL78G13
 *           Processor.
 *   @author DBogdan (dragos.bogdan@analog.com)
********************************************************************************
 * Copyright 2012(c) Analog Devices, Inc.
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *  - Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  - Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *  - Neither the name of Analog Devices, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *  - The use of this software may or may not infringe the patent rights
 *    of one or more patent holders.  This license does not release you
 *    from the requirement that you obtain separate licenses from these
 *    patent holders to use this software.
 *  - Use of the software either in source or binary form, must be run
 *    on or directly connected to an Analog Devices Inc. component.
 *
 * THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT,
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 * IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, INTELLECTUAL PROPERTY RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
********************************************************************************
 *   SVN Revision: 561
*******************************************************************************/

/******************************************************************************/
/* Include Files                                                              */
/******************************************************************************/
#include "Communication.h"
#include <stdio.h>
#include <string.h>
/***************************************************************************//**
 * @brief Initializes the SPI communication peripheral.
 *
 * @param lsbFirst - Transfer format (0 or 1).
 *                   Example: 0x0 - MSB first.
 *                            0x1 - LSB first.
 * @param clockFreq - SPI clock frequency (Hz).
 *                    Example: 1000 - SPI clock frequency is 1 kHz.
 * @param clockPol - SPI clock polarity (0 or 1).
 *                   Example: 0x0 - idle state for SPI clock is low.
 *	                          0x1 - idle state for SPI clock is high.
 * @param clockPha - SPI clock phase (0 or 1).
 *                   Example: 0x0 - data is latched on the leading edge of SPI
 *                                  clock and data changes on trailing edge.
 *                            0x1 - data is latched on the trailing edge of SPI
 *                                  clock and data changes on the leading edge.
 *
 * @return 0 - Initialization failed, 1 - Initialization succeeded.
*******************************************************************************/
unsigned char SPI_Init(unsigned char lsbFirst,
                       unsigned long clockFreq,
                       unsigned char clockPol,
                       unsigned char clockPha)
{
	ADI_CS_HIGH;
	return 1;
}

/***************************************************************************//**
 * @brief Writes data to SPI.
 *
 * @param data - Write data buffer:
 *               - first byte is the chip select number;
 *               - from the second byte onwards are located data bytes to write.
 * @param bytesNumber - Number of bytes to write.
 *
 * @return Number of written bytes.
*******************************************************************************/
unsigned char SPI_Write(unsigned char* data,
                        unsigned char bytesNumber)
{
	unsigned char chipSelect = data[0];
	unsigned char writeData[4] = {0, 0, 0, 0};
	unsigned char readData[4] = {0, 0, 0, 0};
	unsigned char byte = 0;

	for (byte = 0; byte < bytesNumber; byte++) {
		writeData[byte] = data[byte + 1];
	}
	SPI_HandleTypeDef* spi = Get_SPI();
	HAL_StatusTypeDef status;
	for (byte = 0; byte < bytesNumber; byte++) {
		status = HAL_SPI_TransmitReceive(spi, (uint8_t*)&writeData[byte], (uint8_t*)readData, 1, 100);
		while (HAL_SPI_GetState(spi) != HAL_SPI_STATE_READY);
	}
	UART_HandleTypeDef* uart = Get_UART();
	if (status == HAL_OK) {
		char msg[16];
		sprintf(msg, "%s\n", "OK");
		HAL_UART_Transmit(uart, (uint8_t*)msg, strlen(msg), HAL_MAX_DELAY);
	} else if (status == HAL_ERROR) {
		char msg[16];
		sprintf(msg, "%s\n", "ER");
		HAL_UART_Transmit(uart, (uint8_t*)msg, strlen(msg), HAL_MAX_DELAY);
	} else if (status == HAL_BUSY) {
		char msg[16];
		sprintf(msg, "%s\n", "BU");
		HAL_UART_Transmit(uart, (uint8_t*)msg, strlen(msg), HAL_MAX_DELAY);
	} else if (status == HAL_TIMEOUT) {
		char msg[16];
		sprintf(msg, "%s\n", "TO");
		HAL_UART_Transmit(uart, (uint8_t*)msg, strlen(msg), HAL_MAX_DELAY);
	} else {
		char msg[16];
		sprintf(msg, "%s\n", "UK");
		HAL_UART_Transmit(uart, (uint8_t*)msg, strlen(msg), HAL_MAX_DELAY);
	}
	return bytesNumber;
}

/***************************************************************************//**
 * @brief Reads data from SPI.
 *
 * @param data - As an input parameter, data represents the write buffer:
 *               - first byte is the chip select number;
 *               - from the second byte onwards are located data bytes to write.
 *               As an output parameter, data represents the read buffer:
 *               - from the first byte onwards are located the read data bytes. 
 * @param bytesNumber - Number of bytes to write.
 *
 * @return Number of written bytes.
*******************************************************************************/
unsigned char SPI_Read(unsigned char* data,
                       unsigned char bytesNumber)
{
	//HAL_SPI_Receive(Get_SPI(), (uint8_t *) (data + 1), bytesNumber, 100);
	return bytesNumber;
}

