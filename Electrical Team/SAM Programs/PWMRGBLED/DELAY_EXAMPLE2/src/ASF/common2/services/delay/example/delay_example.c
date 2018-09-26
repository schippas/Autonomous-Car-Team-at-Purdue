/**
 * \file
 *
 * \mainpage
 *
 * \section title Delay service example
 *
 * \section file File(s)
 * - \ref delay_example.c
 *
 * Copyright (c) 2011-2018 Microchip Technology Inc. and its subsidiaries.
 *
 * \asf_license_start
 *
 * \page License
 *
 * Subject to your compliance with these terms, you may use Microchip
 * software and any derivatives exclusively with Microchip products.
 * It is your responsibility to comply with third party license terms applicable
 * to your use of third party software (including open source software) that
 * may accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES,
 * WHETHER EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE,
 * INCLUDING ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY,
 * AND FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT WILL MICROCHIP BE
 * LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL
 * LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE
 * SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS BEEN ADVISED OF THE
 * POSSIBILITY OR THE DAMAGES ARE FORESEEABLE.  TO THE FULLEST EXTENT
 * ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY
 * RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 * \asf_license_stop
 *
 */
/*
 * Support and FAQ: visit <a href="https://www.microchip.com/support/">Microchip Support</a>
 */
#include <asf.h>

static void configure_tcc(void);

//! [module_inst]
struct tcc_module tcc_instance;
//! [module_inst]

//! [setup]
static void configure_tcc(void)
{
	struct tcc_config config_tcc;
	tcc_get_config_defaults(&config_tcc, TCC0);
	tcc_get_config_defaults(&config_tcc, TCC1);

	config_tcc.counter.period = 65535;
	config_tcc.compare.wave_generation = TCC_WAVE_GENERATION_SINGLE_SLOPE_PWM;
	config_tcc.compare.match[3] = 65535;
	config_tcc.compare.match[0] = 65535;
	config_tcc.compare.match[1] = 65535;

	config_tcc.pins.enable_wave_out_pin[7] = true;
	config_tcc.pins.wave_out_pin[7] = PIN_PB13F_TCC0_WO7;
	config_tcc.pins.wave_out_pin_mux[7] = MUX_PB13F_TCC0_WO7;

	config_tcc.pins.enable_wave_out_pin[0] = true;
	config_tcc.pins.wave_out_pin[0] = PIN_PB30E_TCC0_WO0;
	config_tcc.pins.wave_out_pin_mux[0] = MUX_PB30E_TCC0_WO0;

	config_tcc.pins.enable_wave_out_pin[1] = true;
	config_tcc.pins.wave_out_pin[1] = PIN_PA09E_TCC0_WO1;
	config_tcc.pins.wave_out_pin_mux[1] = MUX_PA09E_TCC0_WO1;

	tcc_init(&tcc_instance, TCC0, &config_tcc);
	tcc_enable(&tcc_instance);
}

int main(void)
{
	system_init();
	configure_tcc();
	delay_init();

	int devideo = 0;
	//! [main]
	//! [main_loop]
	while (true) {
		devideo	= 65535;
		for (int i = 1; i < 255; i++) {
			devideo = devideo - 255;
			tcc_set_compare_value(&tcc_instance, 3, devideo);
			delay_ms(2);
			
		}
		devideo	= 0;
		for (int i = 1; i < 255; i++) {
			devideo = devideo + 255;
			tcc_set_compare_value(&tcc_instance, 3, devideo);
			delay_ms(2);
			
		}
		devideo	= 65535;
		for (int i = 1; i < 255; i++) {
			devideo = devideo - 255;
			tcc_set_compare_value(&tcc_instance, 0, devideo);
			delay_ms(2);
			
		}
		devideo	= 0;
		for (int i = 1; i < 255; i++) {
			devideo = devideo + 255;
			tcc_set_compare_value(&tcc_instance, 0, devideo);
			delay_ms(2);
			
		}
		devideo	= 65535;
		for (int i = 1; i < 255; i++) {
			devideo = devideo - 255;
			tcc_set_compare_value(&tcc_instance, 1, devideo);
			delay_ms(2);
			
		}
		devideo	= 0;
		for (int i = 1; i < 255; i++) {
			devideo = devideo + 255;
			tcc_set_compare_value(&tcc_instance, 1, devideo);
			delay_ms(2);
			
		}
	}
	//! [main_loop]
	//! [main]
}