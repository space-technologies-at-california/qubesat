/***************************************************************************//**
 *   @file   Communication.h
 *   @brief  Header file of Communication Driver for RENESAS RL78G13 Processor.
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
#ifndef __COMMUNICATION_H__
#define __COMMUNICATION_H__

/******************************************************************************/
/* Include Files                                                              */
/******************************************************************************/
#include "main.h"
/******************************************************************************/
/* GPIO Definitions                                                           */
/******************************************************************************/
#define ADI_PAR_CS_PIN 		GPIO_PIN_10
#define ADI_CS_PIN_OUT      0
#define ADI_CS_LOW          HAL_GPIO_WritePin(GPIOA, ADI_PAR_CS_PIN, GPIO_PIN_RESET);
#define ADI_CS_HIGH         HAL_GPIO_WritePin(GPIOA, ADI_PAR_CS_PIN, GPIO_PIN_SET);

#define GPIO1_PIN              0                     // PSEL
#define GPIO1_PIN_OUT          0
#define GPIO1_PIN_LOW          0
#define GPIO1_PIN_HIGH         0
#define GPIO2_PIN              0           // FSEL
#define GPIO2_PIN_OUT          0
#define GPIO2_PIN_LOW          0
#define GPIO2_PIN_HIGH         0
/******************************************************************************/
/* Functions Prototypes                                                       */
/******************************************************************************/

/* Initializes the SPI communication peripheral. */
unsigned char SPI_Init(unsigned char lsbFirst,
                       unsigned long clockFreq,
                       unsigned char clockPol,
                       unsigned char clockPha);

/* Writes data to SPI. */
unsigned char SPI_Write(unsigned char* data,
                        unsigned char bytesNumber);

/* Reads data from SPI. */
unsigned char SPI_Read(unsigned char* data,
                       unsigned char bytesNumber);

#endif	// __COMMUNICATION_H__
