/*
 * File: my_model.c
 *
 * Code generated for Simulink model 'my_model'.
 *
 * Model version                  : 1.19
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Thu Feb 22 15:41:09 2024
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objective: Execution efficiency
 * Validation result: Passed (4), Warning (1), Error (0)
 */

#include "my_model.h"

/* External inputs (root inport signals with default storage) */
ExtU_my_model_T my_model_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_my_model_T my_model_Y;

/* Real-time model */
static RT_MODEL_my_model_T my_model_M_;
RT_MODEL_my_model_T *const my_model_M = &my_model_M_;

/* Model step function */
void my_model_step(void)
{
  /* Outport: '<Root>/Out1' incorporates:
   *  Gain: '<Root>/Multiply'
   *  Inport: '<Root>/Inp1'
   */
  my_model_Y.Out1 = 2.0 * my_model_U.Inp1;
}

/* Model initialize function */
void my_model_initialize(void)
{
  /* (no initialization code required) */
}

/* Model terminate function */
void my_model_terminate(void)
{
  /* (no terminate code required) */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
