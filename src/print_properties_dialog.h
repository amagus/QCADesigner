//////////////////////////////////////////////////////////
// QCADesigner                                          //
// Copyright 2002 Konrad Walus                          //
// All Rights Reserved                                  //
// Author: Konrad Walus                                 //
// Email: qcadesigner@gmail.com                         //
// WEB: http://qcadesigner.ca/                          //
//////////////////////////////////////////////////////////
//******************************************************//
//*********** PLEASE DO NOT REFORMAT THIS CODE *********//
//******************************************************//
// If your editor wraps long lines disable it or don't  //
// save the core files that way. Any independent files  //
// you generate format as you wish.                     //
//////////////////////////////////////////////////////////
// Please use complete names in variables and fucntions //
// This will reduce ramp up time for new people trying  //
// to contribute to the project.                        //
//////////////////////////////////////////////////////////
// This file was contributed by Gabriel Schulhof        //
// (schulhof@atips.ca).                                 //
//////////////////////////////////////////////////////////
// Contents:                                            //
//                                                      //
// Header for a (fairly) complete print settings dialog //
// with margins, Center Page, paper size, user-selec-   //
// table units (cm/in/pt), etc.                         //
//                                                      //
//////////////////////////////////////////////////////////

#ifndef _PRINT_PROPERTIES_DIALOG_H_
#define _PRINT_PROPERTIES_DIALOG_H_

#include <gtk/gtk.h>
#include "design.h"
#include "print.h"

gboolean get_print_design_properties_from_user (GtkWindow *parent, print_design_OP *pPO, DESIGN *design) ;
void init_print_design_options (print_design_OP *pPO, DESIGN *first_cell) ;

#endif /* _PRINT_PROPERTIES_DIALOG_H_ */
